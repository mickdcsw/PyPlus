Value PORT_NAME (^\S+)

Start
  ^Port.*Type\s*$$ -> ShowPorts

ShowPorts
  ^${PORT_NAME} -> Record

