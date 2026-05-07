import sys
sys.path.insert(0, "/home/kani/devProjects/hill_cipher")

from service.hill_ciphey import encoder, decoder

# Test 1: basic encrypt/decrypt roundtrip
test1 = "adiburai"
enc1 = encoder(test1)
dec1 = decoder(enc1)
print(f"'{test1}' -> '{enc1}' -> '{dec1}'")
# Decrypted text includes padding 'x' chars
assert dec1.startswith(test1), f"Test 1 failed: got {dec1}, expected start with {test1}"
print("Test 1 passed!")

# Test 2: hello
test2 = "hello"
enc2 = encoder(test2)
dec2 = decoder(enc2)
print(f"'{test2}' -> '{enc2}' -> '{dec2}'")
assert dec2.startswith(test2), f"Test 2 failed: got {dec2}, expected start with {test2}"
print("Test 2 passed!")

# Test 3: empty string
test3 = ""
enc3 = encoder(test3)
assert enc3 == "", f"Test 3 failed: got '{enc3}', expected ''"
print("Test 3 passed!")

# Test 4: with special chars and spaces
test4 = "Hello, World!"
enc4 = encoder(test4)
dec4 = decoder(enc4)
expected4 = "helloworld"
print(f"'{test4}' -> '{enc4}' -> '{dec4}'")
assert dec4.startswith(expected4), f"Test 4 failed: got {dec4}, expected start with {expected4}"
print("Test 4 passed!")

# Test 5: exact multiple of 3 (no padding)
test5 = "abcdef"
enc5 = encoder(test5)
dec5 = decoder(enc5)
print(f"'{test5}' -> '{enc5}' -> '{dec5}'")
assert dec5 == test5, f"Test 5 failed: got {dec5}, expected {test5}"
print("Test 5 passed!")

print("\nAll tests passed!")
