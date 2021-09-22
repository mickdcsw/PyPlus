#Value Filldown ROUTER_ID ([0-9\.]+)
#Value Filldown LOCAL_AS (\d+)
Value NEIGHBOR (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value REMOTE_AS (\d+)
Value UP_DOWN (\S+)
Value STATE ((Active|Idle|\d+))

Start
  ^Neighbor.+State.PfxRcd\s*$$ -> Neighbors

Neighbors
  ^${NEIGHBOR}\s+\d*\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE} -> Record

EOF
