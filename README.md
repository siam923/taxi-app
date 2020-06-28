### Postgres setting 
Admin username => postgres
password = 234@siam

## Notes
#### WebSocket & Channel 
The WebSocket protocol works differently then HTTP. Whereas HTTP requests only last as long as the request/response cycle, WebSockets live until one of the two parties involved breaks the connection. Both the client and the server can send each other messages independently over the open connection.

With Django Channels, when the client sends a message to the server, the server sends a message back. The server can also send messages to other connected clients through mechanisms known as channel layers and groups. If a message is broadcast to a group, the server sends the message to every channel in that group.

### Resources
1. Redis -> User for caching. Read more <a href="https://codeburst.io/redis-what-and-why-d52b6829813">Redis</a>
2. Redis on windows: <a href="https://redislabs.com/blog/redis-on-windows-10/">Read the blog</a>
- You need to have a linux subsystem for that.
>My settings: Username: siam   pass: 234@siam

Redis will be used to cache database request. For this we need to all additional layer to channels. Learn about channel layers <a href="https://channels.readthedocs.io/en/latest/topics/channel_layers.html"> Here </a>.

3. Selecting Python Env in vscode: <a href="https://code.visualstudio.com/docs/python/environments">Here</a>.s