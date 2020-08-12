{ pkgs ? import <nixos> {} }:
  pkgs.mkShell {
    buildInputs = [
      pkgs.python38
    ];
}
