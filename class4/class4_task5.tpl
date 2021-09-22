Value DEVICE_ID (\S+)
Value LOCAL_INT (\S+)
Value CAPABILITY (\S+)
Value PORT (\S+)

Start
  ^Device ID.*Port ID -> OUTPUT
  
OUTPUT  
  ^${DEVICE_ID}\s+${LOCAL_INT}\s+\d+\s+${CAPABILITY}\s+${PORT} -> Record
