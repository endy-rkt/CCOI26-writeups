cipher_map = {"A":"a1","B":"a2","C":"a3","D":"b1","E":"b2","F":"b3","G":"c1","H":"c2","I":"c3","J":"a4","K":"a5","L":"a6","M":"b4","N":"b5","O":"b6","P":"c4","Q":"c5","R":"c6","S":"d1","T":"d2","U":"d3","V":"d4","W":"d5","X":"d6","Y":"d7","Z":"d8","a":"e1","b":"e2","c":"e3","d":"f1","e":"f2","f":"f3","g":"g1","h":"g2","i":"g3","j":"e4","k":"e5","l":"e6","m":"f4","n":"f5","o":"f6","p":"g4","q":"g5","r":"g6","s":"h1","t":"h2","u":"h3","v":"h4","w":"h5","x":"h6","y":"h7","z":"h8","0":"i0","1":"i1","2":"i2","3":"i3","4":"i4","5":"i5","6":"i6","7":"i7","8":"i8","9":"i9","+":"j1","/":"j2","=":"j3"}

reverse_map = {v: k for k, v in cipher_map.items()}

descriptions = [
    "c3h7a2a3d7d5b5g6f1d6a1g1d7i3a4e6d8c1d4h3f1c1e6g2e2c2b4g1a6d1a2b2d2h7a2b6d2i1c5g1d3i0g2a2d3e5d3a5c3h7a2c2d8d5i5e6e3f4b3i0d8d5c5i6c3b1c3h5b4e4d3h2b4b1b2h2b4d2d3a5a3e6h2e5d7d6c6g2d7f4b3h8d8d4i0a5e1c1i9h8f1a3a1i9c3b1b2h5a6e4b2h5a6e4d3h5a6e4b2h7a3f5a2h4e3f5c5g1c4d1a1i1b5b1b4h7a3f5d4h8d8d6a4h3d7d5i1e6c3b1",
    "i0g1e3i3d8e4d6i2a4g2d7i2h2i1e3a1g4h5d7d6b5h8f1i2i9h7d8a3a1i9c3b2h1i4e3h7b5c5e3f4i9e5c3d2c3h5b4e4d4i4d5g1f6a5d5i3b5h8e1b3i9g6d8d6e6h8d6c5g4g2d8c1i1g4e2e6i9f6d7d6b5f6c3b1i0g1a4b1d7e5e3f4i9i1e2f4c6h8c4d2d3h5b4b1a1e5e3i2b3h1f1c2b5g2e2c2c5e5e1c1b3h8e1c1d4e5d6i3d8g2e2c2d4e6d6i2g2e6e3f4d4f3e3c1h6g2d7i2d4f6",
    "e2i2h6e5d8d6c3a5a3e6h2g2e3c1e6f1a3f4e6h3f1c1d4h7e2f4b3h1d6i3c6h4e1i2d4h3c3b1i0g1c5i0b5c4d1d6h2h2b4c1i5f3f1c2c3h8e3h8a2h7d6i2b3f3e3d6d3h6d6i3b4i0f1d6c3i0d6i2h5h8d6i3a2h7b4i2i5e5e3e4b5f3c3d1b3i9a3f4g4i3f1b3i9h8d8d5b5h7d8d6c5g1c4d1a2h2f2d4b5i1e3b1b5h7d3h8b5e4e3f4d4i0d1e6f1d3c3d3h2e6f2d2c3h5b4e4d3a5a3e6",
    "h2h8e2d6c6h5d6c5g4h7d8d5h6g2f2d1a1i9c3c2b5h2f1c2a1h3e1d5i5i0d8d6a4h3d7d5h5h3d7i2i9h7e3a1g4i1e3i2d4h7e2f4b3h2d8d1a1i9c3c1b3h1d8d6a4i0e3i0a2e4e2i3a4h5a6f4h6h4d7i2b3h1a3f5a2g2e3i3b5i3e2i3a4e5c3b1i0g1d3i2i0i3e3a3b3d1b4i2h6g2f2d1b4h7b4b1c3i1a3g1j3j3"
]

def decode_description(desc, rev_map):
    result = ''
    i = 0
    while i < len(desc):
        code = desc[i:i+2]
        if code in rev_map:
            result += rev_map[code]
            i += 2
        else:
            result += '?'
            i += 1
    return result

for idx, desc in enumerate(descriptions):
    decoded = decode_description(desc, reverse_map)
    print(f"\nPlaylist {idx+1} (name: inpayloadwetrust{idx*300}):")
    print(f"Decoded: {decoded}")
    import base64
    try:
        final = base64.b64decode(decoded + '==').decode('utf-8', errors='replace')
        print(f"Base64 decoded: {final}")
    except Exception as e:
        print(f"Base64 error: {e}")
