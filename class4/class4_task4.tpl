Value MAC_ADD ([1-9a-f:]+)
Value ADDRESS ([1-9\.]+)
Value NAME ([\d\.]+)
Value INTERFACE (\S+)

Start
  ^MAC Address.+$$ -> OUTPUT

OUTPUT
  ^${MAC_ADD}\s+${ADDRESS}\s+${NAME}\s+{INTERFACE} -> Record
