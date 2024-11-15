import ecdsa
import hashlib
import base58

def generate_private_key():
    """Generates a private key using secp256k1."""
    # Generate a private key object using secp256k1 curve
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    # Convert private key to hexadecimal format
    private_key_hex = private_key.to_string().hex()
    return private_key, private_key_hex

def get_public_key(private_key):
    """Derives the public key from the private key."""
    # Get the public key object
    public_key = private_key.get_verifying_key()
    # Return the public key in uncompressed format (prepend '04' and concatenate x, y coordinates)
    public_key_hex = '04' + public_key.to_string().hex()
    return public_key, public_key_hex

def public_key_to_bitcoin_address(public_key):
    """
    Converts the public key into a Bitcoin address.
    This includes SHA-256, RIPEMD-160, adding a network byte, double SHA-256 checksum,
    and Base58 encoding.
    """
    # Step 1: Perform SHA-256 hash on the public key
    sha256_pubkey = hashlib.sha256(public_key.to_string()).digest()
    
    # Step 2: Perform RIPEMD-160 hash on the SHA-256 result
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_pubkey)
    hashed_pubkey = ripemd160.digest()
    
    # Step 3: Prepend the network byte (0x00 for Bitcoin mainnet)
    network_byte = b'\x00'
    payload = network_byte + hashed_pubkey
    
    # Step 4: Compute the double SHA-256 checksum of the payload
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    
    # Step 5: Append the checksum to the payload
    binary_address = payload + checksum
    
    # Step 6: Base58 encode the binary address
    bitcoin_address = base58.b58encode(binary_address).decode('utf-8')
    return bitcoin_address

def main():
    # Generate a private key
    private_key, private_key_hex = generate_private_key()
    print(f"Private Key (hex): {private_key_hex}")

    # Derive the public key from the private key
    public_key, public_key_hex = get_public_key(private_key)
    print(f"Public Key (hex): {public_key_hex}")

    # Convert the public key to a Bitcoin address
    bitcoin_address = public_key_to_bitcoin_address(public_key)
    print(f"Bitcoin Address: {bitcoin_address}")

if __name__ == "__main__":
    main()
