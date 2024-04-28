# autoKCC

Using [kcc](https://github.com/ciromattia/kcc), i found it very limiting that the docker was basically just a container that needed to be run every time we needed to make a conversion. Also, the file had to be specifically provided every time. AutoKCC comes to respond to those limitations.

autoKCC is a Python program that is based on kcc and adds 2 main features :
- Monitor a folder for new files and automatically convert them based on the user's preferences
- Make the container a running container that doesn't stop after 1 conversion

## Installation

For a simple docker run : 

```bash
docker run --name autokcc --restart unless-stopped \
  -v ./FOLDER1:/input \
  -v ./FOLDER2:/output \
  -e OPTIONS='' \
  ghcr.io/hvmzx/autokcc:main
```

For docker-compose :

```bash
autokcc:
  image: ghcr.io/hvmzx/autokcc:main
  container_name: autokcc
  volumes:
    - /FOLDER1:/input
    - /FOLDER2:/output
  environment:
    - OPTIONS=
```

## Requirements :

- FOLDER1 and FOLDER2 need to be replaced with the folders to mount, respectively matching the folder to monitor and the folder where the processed files will be moved to (both folders can be identical if you do not want to use another folder).
- OPTIONS='' needs to be filled with the kcc options, documentation [here](https://github.com/ciromattia/kcc?tab=readme-ov-file#standalone-kcc-c2epy-usage). DO NOT add the -o option, it is already included and handled with the volume mounting strategy.

## Usage

The input folder will be monitored and for every new manga deposited, it will be processed by kcc and then moved to the output folder.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)