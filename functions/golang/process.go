package functions

import (
	"encoding/json"
	"net/http"
)

type Items struct {
	Items []int `json:"items"`
}

// DecodeRequest parses JSON request into Numbers struct.
func DecodeRequest(r *http.Request) (*Items, error) {
	var items Items
	err := json.NewDecoder(r.Body).Decode(&items)
	return &items, err
}
