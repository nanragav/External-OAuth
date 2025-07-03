from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
from init_utils.logger_init import logger
from cryptography.exceptions import UnsupportedAlgorithm, InvalidKey

def generate_key():

    try:

        current_dir = os.path.dirname(os.path.abspath(__file__))

        priv_path = os.path.join(current_dir, 'keys/private.pem')
        pub_path = os.path.join(current_dir, 'keys/public.pem')

        os.makedirs(os.path.dirname(priv_path), exist_ok=True)

        # Generate a 2048-bit RSA private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Write private key to file
        with open(priv_path, "wb") as f:
            f.write(private_pem)

        public_key = private_key.public_key()

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open(pub_path, "wb") as f:
            f.write(public_pem)

        logger.error("RSA private and public keys generated successfully.")

    except UnsupportedAlgorithm as e:

        logger.error(f"Unsupported algorithm: {e}")

    except ValueError as e:

        logger.error(f"Value error during key generation/serialization: {e}")

    except InvalidKey as e:

        logger.error(f"Invalid key encountered: {e}")

    except OSError as e:

        logger.error(f"File I/O error: {e}")

    except Exception as e:

        logger.error(f"Unexpected error: {e}")
