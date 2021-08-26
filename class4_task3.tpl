Value INT_NAME (Ethernet\d+/\d+)
Value LINE_STATE ((up|down))
Value ADMIN_STATE ((up|down))
Value MAC_ADD (\S+)

Start
  ^${INT_NAME} is ${LINE_STATE}
  ^admin state is ${ADMIN_STATE}
  ^\s+Hardware:\s+Ethernet,\s+address:\s+${MAC_ADD} -> Record
