package functions

import (
	"encoding/json"
	"net/http"
)

type Numbers struct {
	Numbers []int `json:"numbers"`
}

// DecodeRequest parses JSON request into Numbers struct.
func DecodeRequest(r *http.Request) (*Numbers, error) {
	var nums Numbers
	err := json.NewDecoder(r.Body).Decode(&nums)
	return &nums, err
}
