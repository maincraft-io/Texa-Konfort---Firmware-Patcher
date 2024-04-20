## Script for Patching and Uploading Texa 720R Firmware

This script is designed to help you modify Texa 720R firmware for downgrading, reinstalling, or applying custom patches.

**Instructions:**

1. Place your `texa.py` script in the same directory as the `knf_app.ini` file.

**Force Update Modes:**

* **Enabled:** To enable force update mode, run the script with the following command:
```bash
python texa.py 1
```
Copy the updated file to an SD card and use it to update your Texa 720R device.

* **Disabled:** To disable force update mode, run the script with this command:
```bash
python texa.py 0 
```
Copy the modified file to an SD card and perform an update on your Texa 720R device.

**Enjoy your customized firmware!**

**Important Notes:**

* Firmware modifications can potentially harm your device. Proceed with caution and at your own risk.
* Make sure you have the necessary dependencies and that the `knf_app.ini` file is formatted correctly before proceeding.

**Disclaimer:**

The use of this script is entirely at your own risk. The authors are not responsible for any damages or malfunctions that may arise from its use.
