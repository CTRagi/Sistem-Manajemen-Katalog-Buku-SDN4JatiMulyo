"""Pengganti hashlib.pbkdf2_hmac untuk Python Workers.

Runtime Python 3.14 di Cloudflare Workers tidak punya hashlib.pbkdf2_hmac,
padahal Werkzeug memakainya untuk membuat dan memeriksa hash kata sandi.
Modul ini menggantinya dengan Web Crypto bawaan Workers (cepat, native).
Hasilnya identik dengan versi OpenSSL, jadi format hash Werkzeug tidak berubah.
"""
import hashlib

from pyodide.ffi import run_sync, to_js

_ALGO = {"sha1": "SHA-1", "sha256": "SHA-256", "sha384": "SHA-384", "sha512": "SHA-512"}
_BITS = {"sha1": 160, "sha256": 256, "sha384": 384, "sha512": 512}


def _pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None):
    # Diimpor di sini (bukan di atas file) supaya tidak ada objek JavaScript
    # yang tertahan di lingkup global saat Worker dimulai.
    from js import Object, Uint8Array, crypto

    name = hash_name.lower().replace("-", "")
    bits = dklen * 8 if dklen else _BITS[name]
    key = run_sync(
        crypto.subtle.importKey("raw", to_js(password), "PBKDF2", False, to_js(["deriveBits"]))
    )
    # dict_converter wajib: tanpa ini Pyodide mengubah dict menjadi Map, bukan objek biasa.
    params = to_js(
        {"name": "PBKDF2", "hash": _ALGO[name], "salt": to_js(salt), "iterations": iterations},
        dict_converter=Object.fromEntries,
    )
    derived = run_sync(crypto.subtle.deriveBits(params, key, bits))
    return Uint8Array.new(derived).to_bytes()


# Hanya dipasang kalau runtime memang tidak punya fungsinya.
if not hasattr(hashlib, "pbkdf2_hmac"):
    hashlib.pbkdf2_hmac = _pbkdf2_hmac
