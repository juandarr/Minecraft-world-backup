# Minecraft backup script

## How it works

### Python script

The main script `minecraft_backup.py` implements three different steps aimed to safely stop, backup and reboot the minecraft world running on the server.

- Step 1: stops the server. This script will store the users and chunks for the overworld, nether and the end. This will safely store the current data of the world and will avoid file corruption since the server is stopped. 

- Step 2: creates a backup of the world, nether and the end. To do this the script uses the modules `shutils`, `subprocess` and `datetime`. 
	- `shutils`: used to create a whole copy of a tree directory and move it to a specific location. 
	- `subprocess`: allows to execute arbitrary commands in Bash
	- `datetime`: gives us the current date and time.

- Step 3: reboots the server. As a maintenance task it is important to reset the background processes, RAM, cache and other aspects of a computer. Rebooting the server allows to start from a blank slate, sometimes fixing problems and giving a boost in speed

### Bash script

The job of this script is to run the Python script. I was careful of using absolute paths in both the Python and Bash scripts to avoid trouble referencing paths. 

## Dependencies

The modules `shutils`, `subprocess` and `datetime` are part of the standard Python library.  

## Cron job

After completing the Python and Bash scripts, the final step is the definition of a new cron job. This is implemented via `crontab -e` and adding a new line according to the instructions from this [Crontab](https://www.computerhope.com/unix/ucrontab.htm)'s page. 
