import ssl
import socket

class ETSIComplianceEngine:
    """
    Automated Auditor for ETSI EN 303 645 Provision 5: Secure Communications
    """

    def __init__(self, device_ip, port=443):
        self.target = (device_ip, port)

    def audit_tls_compliance(self):
        context = ssl.create_default_context()

        try:
            with socket.create_connection(self.target, timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.target[0]) as ssock:
                    cipher = ssock.cipher()
                    version = ssock.version()

                    is_compliant = version in ['TLSv1.2', 'TLSv1.3']

                    return {
                        "Provision": "5.1-1",
                        "Check": "Secure Communication (TLS)",
                        "Status": "PASS" if is_compliant else "FAIL",
                        "Protocol": version,
                        "Cipher": cipher[0]
                    }

        except Exception as e:
            return {
                "Provision": "5.1-1",
                "Status": "INCONCLUSIVE",
                "Error": str(e)
            }


# ---- RUN SCRIPT ----
if __name__ == "__main__":
    target = input("Enter domain or IP (e.g. google.com): ")

    engine = ETSIComplianceEngine(target)
    result = engine.audit_tls_compliance()

    print("\n=== ETSI Compliance Result ===")
    for key, value in result.items():
        print(f"{key}: {value}")