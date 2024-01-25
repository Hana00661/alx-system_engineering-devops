*How to create SSH keys?
1- Generate the key pair:
	Run the ssh-keygen command. You can customize the key type and filename with optional flags:

Default: ssh-keygen (creates an RSA key with the default filename)
Specify key type: ssh-keygen -t rsa (RSA) or ssh-keygen -t ed25519 (Ed25519)
Specify filename: ssh-keygen -f my_ssh_key (saves private key as my_ssh_key)

2-  Enter a passphrase (optional):

	When prompted, enter and confirm a strong passphrase for additional security. You can skip this step, but be aware that the private key will be unencrypted.

3- (Optional) Add the public key to your remote server:

Copy the contents of the public key file (id_rsa.pub) and add it to the authorized_keys file on your server. Refer to your server's documentation for specific instructions.

Additional tips:

Consider using a longer passphrase (12+ characters) for strong security.
Backup your private key securely, as losing it will lock you out of your server.
Avoid using the same passphrase for multiple keys.

