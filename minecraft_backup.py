import subprocess as sp
import shutil as sh
from datetime import datetime

#1. Stop the minecraft server
sp.call(['/home/pi/minecraft/stop'])
print('Step 1 completed: Server has been stoped in script')

#2. After veryfication of exit server, backup the minecraft world
sources_to_copy = {'world':'/home/pi/minecraft/world', 'world_nether':'/home/pi/minecraft/world_nether', 'world_the_end':'/home/pi/minecraft/world_the_end'}

destination_root = '/home/pi/minecraft_backups/'

world_identifier = 'mountainHome'
now = datetime.now()

destination_folder = destination_root + '{5}-{2}-{1}-{0}_t{3}:{4}'.format(now.day,now.month,now.year,now.hour,now.minute, world_identifier)
print(destination_folder)

for sourceKey, source in sources_to_copy.items():
    sh.copytree(source, destination_folder+'/'+sourceKey)
    print('Backup of '+ sourceKey + ' completed')
print('Step 2:........\nBackup completed!')

#3. Reboot the server
print('Step 3: Rebooting')
sp.call(['sudo', '/home/pi/minecraft/reboot'])
