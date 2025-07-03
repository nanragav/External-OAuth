from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, UTC
import os
from init_utils.logger_init import logger
from cryptography.exceptions import InvalidSignature, UnsupportedAlgorithm

def cert_gen():

    try:

        current_dirt = os.path.dirname(os.path.abspath(__file__))

        key_file = os.path.join(current_dirt, 'certs/key.pem')
        cert_file = os.path.join(current_dirt, 'certs/cert.pem')

        os.makedirs(os.path.dirname(key_file), exist_ok=True)

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        with open(key_file, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        logger.error(f"Private key saved to: {key_file}")

        # Generate self-signed X.509 certificate
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"IN"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u""),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u""),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u""),
            x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
        ])

        certificate = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.now(UTC)
        ).not_valid_after(
            # Certificate valid for 365 days
            datetime.now(UTC) + timedelta(days=365)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
            critical=False,
        ).sign(private_key, hashes.SHA256())

        # Write certificate to .crt file
        with open(cert_file, "wb") as f:
            f.write(certificate.public_bytes(serialization.Encoding.PEM))

        logger.error(f"Certificate saved to: {cert_file}")


    except FileNotFoundError as e:

        logger.error(f"Directory or file not found: {e}")

    except PermissionError as e:

        logger.error(f"Permission denied while writing key or cert: {e}")

    except ValueError as e:

        logger.error(f"Value error: {e}")

    except UnsupportedAlgorithm as e:

        logger.error(f"Unsupported algorithm used: {e}")

    except InvalidSignature as e:

        logger.error(f"Invalid signature during cert signing: {e}")

    except OSError as e:

        logger.error(f"OS error: {e}")

    except Exception as e:

        logger.error(f"Unexpected error: {e}")
