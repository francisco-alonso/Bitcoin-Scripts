#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>
#include <ctime>
#include <cmath>
#include <limits>

using namespace std;

// Global constants
const uint32_t max_nonce = 4294967296; // 2^32 (4 billion)
const uint32_t max_difficulty = 32;    // from 0 to 31 bits

// Function to calculate SHA-256 hash of a string
string sha256(const string &input) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, input.c_str(), input.size());
    SHA256_Final(hash, &sha256);

    stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    }
    return ss.str();
}

// Proof of Work function
pair<string, uint32_t> proof_of_work(const string &header, uint32_t difficulty_bits) {
    uint64_t target = 1ULL << (256 - difficulty_bits);

    for (uint32_t nonce = 0; nonce < max_nonce; ++nonce) {
        string hash_result = sha256(header + to_string(nonce));
        
        // Convert hash_result to an integer for comparison
        uint64_t hash_int;
        stringstream ss;
        ss << hex << hash_result;
        ss >> hash_int;

        if (hash_int < target) {
            return make_pair(hash_result, nonce);
        }
    }

    cout << "Failed after " << max_nonce << " tries" << endl;
    return make_pair("", max_nonce);
}

int main() {
    uint32_t nonce = 0;
    string hash_result;

    for (uint32_t difficulty_bits = 0; difficulty_bits < max_difficulty; ++difficulty_bits) {
        uint32_t difficulty = 1 << difficulty_bits;
        cout << "Difficulty: " << difficulty << " (" << difficulty_bits << " bits)" << endl;

        cout << "Starting search..." << endl;

        // Checkpoint the current time
        clock_t start_time = clock();

        // We fake a block of transactions and add the hash of the previous block
        string new_block = "My name is Francisco Lopez and my transactions are here" + hash_result;

        // Calculate PoW for the current block with the given difficulty
        tie(hash_result, nonce) = proof_of_work(new_block, difficulty_bits);

        // Calculate elapsed time
        clock_t end_time = clock();
        double elapsed_time = double(end_time - start_time) / CLOCKS_PER_SEC;

        cout << "Elapsed time: " << elapsed_time << " seconds" << endl;

        // Calculate hashing power
        if (elapsed_time > 0) {
            double hash_power = nonce / elapsed_time;
            cout << "Hashing power: " << hash_power << " hashes per second" << endl;
        }
    }
    return 0;
}
