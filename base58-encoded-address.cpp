/*
The code generates a Bitcoin public key and corresponding P2PKH (Pay-to-Public-Key-Hash) address from a given private key using the libbitcoin library. This is a common operation in Bitcoin software for creating wallet addresses
*/
#include <bitcoin/bitcoin.hpp>

int main() {
    bc::ec_secret decoded;
    bc::decode_base16(decoded, "1E99423A4ED27608A15A2616C1B3F455BE7A97E88718A8E4A9B8F1C52A32D793");

    bc::wallet::ec_private secret(
        decoded, bc::wallet::ec_private::mainnet_p2kh
    ); // mainnet format

    // Get PubK
    bc::wallet::ec_public public_key(secret);
    std::cout << "Public key: " << public_key.encoded() << std::endl;

    // Compute hash of PubK for P2PKH address
    bc::data_chunk public_key_data;
    public_key.to_data(public_key_data);

    const auto hash = bc::bitcoin_short_hash(public_key_data);

    bc::data_chunk unencoded_address;
    unencoded_address.reserve(25);  // 25B for version, hash, and checksum
    unencoded_address.push_back(0);

    bc::extend_data(unencoded_address, hash);
    bc::append_checksum(unencoded_address); 

    assert(unencoded_address.size() == 25);

    const std::string address = bc::encode_base58(unencoded_address);

    std::cout << "Address: " << address << std::endl;

    return 0;
}
