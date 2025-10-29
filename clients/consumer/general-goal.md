# General Goal and Flow for a Consumer

### For a given consumer: (DONE)
- define your consumer connection creds (username, password, connection points, etc)

- establish a connection to desired endpoint

- begin consuming data


### For a given message from the broker:

- ingest data over the established connection

- process the data based on content/format
	- if data is of XYZ format/content type
		- process that data
	- else
		- return error msg

### For a given message processing action:

- extract and transform desried data and map to another data type
	- ex: string/json to list/dict (potentially for a data dropdown on a frontend application)
- distribute new data type to another process 