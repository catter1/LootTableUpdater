# LootTableUpdater
Python program made in order to update loot tables each time Mojang changes them. For now, the singular program defines the "type" in count functions where it is not defined.

**How to Use**
- Make sure your system is able to execute Python programs.
- Put the file in the directory of the loot tables you want modified.
- Run `python lootupdater.py [file/all] {bypass}`
  - In `[file/all]`, specify what file you want modified, or type `all` to modify all files in the directory appended in `.json`.
    - **WARNING**: If you select `all`, the program will continue, even if a `.json` file is not valid. 
  - If you are getting an error for an individual file about it not being a valid JSON format, the `bypass` option is available as a second argument to modify the file anyways.
- When program is complete, it will give a success message, along with telling you what files were modified (and how many times `"type"` was added).

**Want to Use This?**
- Feel free. (It's public for a reason!) Just don't claim it as your own, or give credit to `catter1` if used in large project.
