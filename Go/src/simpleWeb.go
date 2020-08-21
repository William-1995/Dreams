package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/hello", handler)
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

//The handler echoes the path part of the request URL r

func handler(w http.ResponseWriter, r * http.Request) {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}
