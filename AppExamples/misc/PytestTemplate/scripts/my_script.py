"""Minimal script to test the ZEISS INSPECT Python API connection."""
import gom

print("Hello from my_script.py")
print(f"ZEISS INSPECT version: {gom.app.application_build_information.version}")
