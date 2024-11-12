# BTC Notes

## Getting unspent outputs of a public address

```
curl https://blockchain.info/unspent?active={{address}}
curl https://blockchain.info/unspent?active=1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK
```

```
{
  "notice": "",
  "unspent_outputs": [
    {
      "tx_hash_big_endian": "ce3454376a468f3fa7f241355724dd340fde63b9e51d7da3c3197a97691d0534",
      "tx_hash": "34051d69977a19c3a37d1de5b963de0f34dd24573541f2a73f8f466a375434ce",
      "tx_output_n": 1,
      "script": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
      "value": 9978,
      "value_hex": "26fa",
      "confirmations": 233403,
      "tx_index": 1830290334084931
    },
    {
      "tx_hash_big_endian": "b45a9cb4a1061b7c48752757c44c28575051366483c54c9934036130c4752289",
      "tx_hash": "892275c430610334994cc5836436515057284cc4572775487c1b06a1b49c5ab4",
      "tx_output_n": 1,
      "script": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
      "value": 6236,
      "value_hex": "185c",
      "confirmations": 322484,
      "tx_index": 4824995125922848
    },
    {
      "tx_hash_big_endian": "ee5f17e9d821ca5d3ad7b221ba48820e8301a79e57a8660c7ac1b8db2b5c34bd",
      "tx_hash": "bd345c2bdbb8c17a0c66a8579ea701830e8248ba21b2d73a5dca21d8e9175fee",
      "tx_output_n": 1,
      "script": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
      "value": 3020,
      "value_hex": "0bcc",
      "confirmations": 354516,
      "tx_index": 6657042634471192
    }
    ]
}
```

#### UTXO Response Parameters

Each unspent transaction output (UTXO) returned from the API contains several important fields:

- **`tx_hash_big_endian`**: 
  - Transaction hash in "big-endian" format (most significant byte first).
  - A 64-character hexadecimal string uniquely identifying the transaction.

- **`tx_hash`**: 
  - Transaction hash in "little-endian" format (least significant byte first), commonly used in Bitcoin explorers.
  - This is the reverse of `tx_hash_big_endian`.

- **`tx_output_n`**: 
  - Output index number within the transaction.
  - Each transaction can contain multiple outputs; this number identifies which output this UTXO represents, starting from 0.

- **`script`**: 
  - The `scriptPubKey` for the output, in hexadecimal format.
  - Specifies the conditions needed to spend this output, typically containing a locking script.  
  - Example script: `76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac`, which represents a Pay-to-PubKey-Hash (P2PKH) script.

- **`value`**: 
  - The amount of Bitcoin available in this output, in satoshis (1 BTC = 100,000,000 satoshis).

- **`value_hex`**: 
  - The value in hexadecimal format, representing the same amount as `value` but in hexadecimal.

- **`confirmations`**: 
  - The number of confirmations this output has received.
  - A higher number indicates greater security and inclusion in multiple blocks.

- **`tx_index`**: 
  - A unique identifier for this transaction output in the `blockchain.info` database.
  - Useful for tracking within their system, though it may not be required in most Bitcoin applications.


