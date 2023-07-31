detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_linux
            ;;
        "Ubuntu")
            install_linux
            ;;
        *)
            echo "[*] Unsupported platform: $platform"
            ;;
    esac
}
install_linux(){
    sudo echo "sudo python $HOME/.dx4/example/main.py \$1 \$2 \$3 \$4 \$5" > $HOME/.local/bin/example
    sudo mkdir -p $HOME/.dx4
    sudo echo 'echo "[*] Uninstalling example..." && sudo rm -rf $HOME/.dx4/example && sudo rm -rf $HOME/.local/bin/example && sudo rm -rf $HOME/.local/bin/example-uninstaller && echo "[*] example uninstall task done"' > $HOME/.local/bin/example-uninstaller
    sudo cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.dx4/example"
    sudo chmod +x $HOME/.local/bin/example
    sudo chmod +x $HOME/.local/bin/example-uninstaller
}
install_termux(){
    mkdir -p $HOME/.dx4
    cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.dx4/example"
    echo "python $HOME/.dx4/example/main.py \$1 \$2 \$3 \$4 \$5" > $PREFIX/bin/example
    echo 'echo "[*] Uninstalling example..." && rm -rf $HOME/.dx4/example && rm -rf $PREFIX/bin/example && rm -rf $PREFIX/bin/example-uninstaller && echo "[*] example uninstall task done"' > $PREFIX/bin/example-uninstaller
    chmod +x $PREFIX/bin/example
    chmod +x $PREFIX/bin/example-uninstaller
}
detect_platform