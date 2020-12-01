package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
	"os"
)

func base16() {
	fmt.Printf("input:\n")
	var buffer [512]byte
	n, err := os.Stdin.Read(buffer[:])
	if err != nil {
		panic(err)
	}
	encoded := hex.EncodeToString(buffer[:n])
	fmt.Printf("encoded: %s\n", encoded)

	decoded, err := hex.DecodeString(encoded)
	if err != nil {
		panic(err)
	}
	fmt.Printf("decoded: %s\n", decoded)
}

func testbase64() {
	fmt.Printf("input:->\n")
	var buffer [512]byte
	n, err := os.Stdin.Read(buffer[:])
	if err != nil {
		panic(err)
	}
	encoded := base64.StdEncoding.EncodeToString(buffer[:n])
	fmt.Printf("sEnc: %s\n", encoded)

	sDec, _ := base64.StdEncoding.DecodeString(encoded)
	fmt.Printf("sDec: %s\n", sDec)

	uEnc := base64.URLEncoding.EncodeToString(buffer[:n])
	fmt.Printf("uEnc: %s\n", uEnc)

	uDec, _ := base64.URLEncoding.DecodeString(uEnc)
	fmt.Printf("uDec: %s\n", uDec)

}
