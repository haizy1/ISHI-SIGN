from datetime import datetime, timedelta
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.x509.oid import NameOID

def generate_self_signed_certificate(private_key_path, certificate_path):
    # Générer la clé privée RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Générer le certificat
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Organization"),
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US")
    ])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=365)
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True
    ).sign(private_key, hashes.SHA256())

    # Enregistrer la clé privée et le certificat auto-signé
    with open(private_key_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    with open(certificate_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

def sign_document(private_key_path, certificate_path, document_path, signature_path):
    # Charger la clé privée et le certificat
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(), password=None
        )
    with open(certificate_path, "rb") as f:
        certificate = x509.load_pem_x509_certificate(f.read())

    # Charger le document à signer
    with open(document_path, "rb") as f:
        document = f.read()

    # Signer le document
    signature = private_key.sign(
        document,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Enregistrer la signature
    with open(signature_path, 'wb') as sig_file:
        sig_file.write(signature)

    # Vérifier la signature
    public_key = certificate.public_key()
    try:
        public_key.verify(
            signature,
            document,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("La signature est valide")
    except:
        print("La signature est invalide")

# Exemple d'utilisation
private_key_path = 'private_key.pem'
certificate_path = 'certificate.pem'
# document_path = 'lettre_motivation.pdf'
#signature_path = 'lettre_signed.bin'



document_path = input("Entrez le chemin d'accès pour le document à signer : ")
signature_path = input("Entrez le chemin d'accès pour la signature : ")
# Génération du certificat auto-signé
generate_self_signed_certificate(private_key_path, certificate_path)

# Signature du document et vérification de la signature
sign_document(private_key_path, certificate_path, document_path, signature_path)
