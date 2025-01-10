from paramiko import AutoAddPolicy, SSHClient

class SSHUtils:
  """Paramiko wrapper to provide ssh utilities"""
  def __init__(self, hostanme: str, username: str, password: str, port: int = 22):
    """Initialize the values"""
    self.client = SSHClient()
    self.hostname = hostname
    self.port = port
    self.username = username
    self.password = password

  def connect(self):
    """Connect to the hostname provided on the init"""
    try:
      self.client.set_missing_host_key_policy(AutoAddPolicy())
      self.client.connect(
        hostname=self.hostname,
        username=self.username,
        password=self.password,
        port=self.port,
      )
      self.logger.info(f"Connection to {self.hostname} has been established")
      
    except Exception as e:
      self.logger.error(f"Error: {e}")

  def _sftp(self):
    """Enable SFTP conneciton"""
    return self.client.open_sftp()

  def disconnect(self):
    """Close connections if they are open"""
    self.client.close()
    self.logger.info(f"Connection to {self.hostname} has been closed")

  def exec_command(self, command: str) -> list:
    """This function is design to run one command at a time for a purpose"""
    stdin, stdout, stderr = self.client.exec_command(command)
    status = stdout.channel.recv_exit_status()

    if status == 0:
      return stdout.read().decode().strip().splitlines()
    else:
      self.logger.warning(f"Command: '{command}' did not run succesfully")
      return stderr.read().decode().strip().splitlines()

  def upload(self, local_path: str, remote_path: str) -> None:
    """Upload a file using sftp"""
    try:
      sftp = self._sftp()
      sftp.put(local_path, remote_path)
      sftp.close()
      self.logger.info(f"File has been uploaded to {self.hostname}:{remote_path}")

    except:
      self.logger.error(f"File transfer has failed due to an error: {e}")

  
  def download(self, local_path: str, remote_path: str) -> None:
    """Upload a file using sftp"""
    try:
      sftp = self._sftp()
      sftp.get(remote_path, local_path)
      sftp.close()
      self.logger.info(f"File has been uploaded to {self.hostname}:{remote_path}")

    except:
      self.logger.error(f"File transfer has failed due to an error: {e}")


    
      
