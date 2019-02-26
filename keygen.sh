# lets create a key to sign these tokens with
openssl genpkey -out mykey.pem -algorithm rsa -pkeyopt rsa_keygen_bits:2048 
# lets generate a public key for it...
openssl rsa -in mykey.pem -out mykey.pub -pubout 