import hashlib
from Crypto.Util.number import long_to_bytes

# ==========================================
# 1. SETUP PARAMETERS
# ==========================================
# p is the Mersenne prime M521 used for the finite field
p = 2**521 - 1
EXPECTED_SHA256 = "f687cb74fdcefefc"

# The 5 perfect shares we know are 100% correct (from the highlands)
shares = [
    (1, 0xd0393fd5aa76c02f53757a5883d97a0f0ade112cffc590c8378f2b5a6696a284dcc1ef10c29f7275958952bca3c40922f75258f47e808d587aca867f48f0d798f5),
    (2, 0xa0deb8650c459c78e99ca5ae29c1399c8221723e6c966a4a4494ec69bcb20399336bba13c10998b4b0b554cffdaec9b8b536e6fa9ea4eefa7321782797b84672e4),
    (3, 0x9dc6d639cbda2c6893efafe086027e1f9126a9e27f2d342e45e8090675c2eca7e4ae330b163f8f059fa665a20ea4be41a4de9fe882ac3b08387ba8649622293745),
    (4, 0xff3a80c762b7a71ee3793ed87a7951f819960a86b067cefbe94cac78b9f556291ebf42ae21395da1a5e9d3d426624b6cf5bebb4487d9311737417749e401c0cb57),
    (5, 0x748755843bdf0733e28882bb8f096fdd4c4ae2142cba5fb2ea4ba7e65a7b007a75f34a4f7a94b4b8e5b9d425d415b5750066cb52e451f11933b086614b816d4ecb)
]

# We only need ONE flooded station to get our 6th point (k=6)
# We will use Saint-Benoit (x = 6). 
x_partial = 6
y_partial_base = 0x18e91e304d2372e99ce65481f4a15284c423aa9ac47a25b639109b2c0c5d60cb6ba133679b80d2d34cfdc2c2968c5b83977eaa1b6e5ad7ed0368e3d0a9639300000

# Our list of 6 x-coordinates
xs = [x for x, y in shares] + [x_partial]

# ==========================================
# 2. MATH PRECOMPUTATION (Optimization)
# ==========================================
# Function to calculate the Lagrange basis polynomial evaluated at x=0
def get_L0(i, xs, p):
    num, den = 1, 1
    for j in xs:
        if j != i:
            num = (num * (-j)) % p
            den = (den * (i - j)) % p
    # multiply by the modular inverse of the denominator
    return (num * pow(den, -1, p)) % p

print("[*] Calculating Lagrange basis for our 6 points...")
L = [get_L0(x, xs, p) for x in xs]

print("[*] Precomputing the static part C...")
# Precompute C = sum of (y_i * L_i) for the 5 intact shares + the base of the 6th
C = 0
for i in range(5):
    C = (C + shares[i][1] * L[i]) % p

# Add the base (flooded) contribution of the 6th share
C = (C + y_partial_base * L[5]) % p

# The only thing that changes when delta increases by 1 
# is we add 1 * L[5] to our secret.
step = L[5]

# ==========================================
# 3. BRUTE FORCE
# ==========================================
print("[*] Starting fast brute force for 2^20 (1,048,576) possibilities...")
current_secret = C

for delta in range(2**20):
    # Instead of doing massive math, we only do one simple addition per loop!
    # current_secret represents S(delta)
    
    try:
        # Convert integer to bytes to check if it's readable text
        secret_bytes = long_to_bytes(current_secret)
        
        # Check if it starts with the flag format
        if secret_bytes.startswith(b'CCOI26{'):
            # Double check with the SHA256 hash provided in the challenge
            sha256_hash = hashlib.sha256(secret_bytes).hexdigest()
            if sha256_hash.startswith(EXPECTED_SHA256):
                print(f"\n[+]Match found at delta = {delta}")
                print(f"[+] The secret polynomial P(0) is: {current_secret}")
                print(f"[+] Flag: {secret_bytes.decode('ascii')}")
                break
    except Exception:
        # long_to_bytes will fail or produce garbage if the number isn't valid text
        pass
    
    # Mathematical optimization: S(delta + 1) = S(delta) + L_6(0)
    current_secret = (current_secret + step) % p
