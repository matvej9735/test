#!/bin/sh
mkdir -p /data

if [ -n "$SESSION_B64" ]; then
    python3 -c "
import base64, zlib, os
b64 = os.environ['SESSION_B64']
data = zlib.decompress(base64.b64decode(b64))
with open('/data/tg_userbot.session', 'wb') as f:
    f.write(data)
"
fi

if [ -f /app/tg_userbot.session ]; then
    cp -n /app/tg_userbot.session /data/tg_userbot.session 2>/dev/null || true
fi

cd /data

while true; do
    python /app/main.py
    sleep 10
done
