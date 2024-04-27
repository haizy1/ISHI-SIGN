from datetime import datetime, timedelta
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

def generate_self_signed_certificate():
    """Generate a new self-signed X.509 certificate with the user's input."""

    # Prompt the user for the certificate information
    common_name = input("Enter the Common Name (e.g. example.com): ")
    country_name = input("Enter the Country Name (2-letter code): ")
    state_or_province_name = input("Enter the State or Province Name: ")
    locality_name = input("Enter the Locality Name (e.g. city): ")
    organization_name = input("Enter the Organization Name: ")

    # Generate a new RSA key pair
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Set the certificate subject and issuer information
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country_name),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state_or_province_name),
        x509.NameAttribute(NameOID.LOCALITY_NAME, locality_name),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization_name),
        x509.NameAttribute(NameOID.COMMON_NAME, common_name),
    ])

    # Set the certificate valid time period
    now = datetime.utcnow()
    cert_duration = timedelta(days=365)
    cert_not_before = now - timedelta(days=1)
    cert_not_after = cert_not_before + cert_duration

    # Build the certificate object
    cert_builder = x509.CertificateBuilder()
    cert_builder = cert_builder.subject_name(subject)
    cert_builder = cert_builder.issuer_name(issuer)
    cert_builder = cert_builder.not_valid_before(cert_not_before)
    cert_builder = cert_builder.not_valid_after(cert_not_after)
    cert_builder = cert_builder.serial_number(x509.random_serial_number())
    cert_builder = cert_builder.public_key(key.public_key())
    cert_builder = cert_builder.add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True
    )

    # Sign the certificate using the private key
    certificate = cert_builder.sign(
        private_key=key,
        algorithm=hashes.SHA256(),
    )

    # Write the certificate and private key to files
    cert_filename = f"{common_name}.crt"
    key_filename = f"{common_name}.key"
    with open(cert_filename, "wb") as cert_file:
        cert_file.write(certificate.public_bytes(serialization.Encoding.PEM))
    with open(key_filename, "wb") as key_file:
        key_file.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))

    print(f"Certificate written to '{cert_filename}'")
    print(f"Private key written to '{key_filename}'")

if __name__ == "__main__":
    generate_self_signed_certificate()
