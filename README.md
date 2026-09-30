# Password Manager — Tkinter Learning Demo

A small desktop exercise in Tkinter forms, password generation and local file handling. It generates a password, copies it to the clipboard and can save a website/email/password entry locally.

## Run

Use Python 3 with Tkinter available, install `python -m pip install -r requirements.txt`, and run `python main.py` from this directory. Tkinter may require a separate operating-system package on Linux.

## What it demonstrates

`main.py` contains the form, input checks, clipboard integration and file-writing exercise. Random choices use Python's cryptographically backed `SystemRandom`.

## Security boundary

This is **not a secure credential vault**. Saved entries are plaintext in `data.txt`, and generated values are copied to the system clipboard. Use made-up demonstration data only. The local data file is ignored by Git. Removing the previously committed file does not erase earlier Git history; replace any real password that was saved in it.

A production password manager would need an audited encrypted vault, key derivation, access controls and a separate security design. This repository makes no such claim.
