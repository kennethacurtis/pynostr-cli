# pynostre_cli/key.py
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def generate_key_pair(format):
    # Generate a new secp256k1 key pair
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())

    # Extract the public key
    public_key = private_key.public_key()

    if format == 'pem':
      # Serialize the private key to PEM format
      private_key = private_key.private_bytes(
          encoding=serialization.Encoding.PEM,
          format=serialization.PrivateFormat.PKCS8,
          encryption_algorithm=serialization.NoEncryption()
      )

      # Serialize the public key to PEM format
      public_key = public_key.public_bytes(
          encoding=serialization.Encoding.PEM,
          format=serialization.PublicFormat.SubjectPublicKeyInfo
      )

      private_key = private_key.decode()
      public_key = public_key.decode()

    else:
      # Convert the keys to hexadecimal strings
      private_key = private_key.private_numbers().private_value
      public_key = public_key.public_bytes(
          encoding=serialization.Encoding.X962,
          format=serialization.PublicFormat.UncompressedPoint
      ).hex()

    return private_key, public_key