package main

import (
    "context"
    "net/http"
    "encoding/json"
    "app/functions"
    kitendpoint "github.com/go-kit/kit/endpoint"
    kithttp "github.com/go-kit/kit/transport/http"
)

type Response struct {
    Result interface{} `json:"result"`
}


func makeComputeEndpoint() kitendpoint.Endpoint {
    return func(ctx context.Context, request interface{}) (interface{}, error) {
        req := request.(*functions.Numbers)
        return Response{Result: functions.Compute(req.Numbers)}, nil
    }
}

func makeMultiplyEndpoint() kitendpoint.Endpoint {
    return func(ctx context.Context, request interface{}) (interface{}, error) {
        req := request.(*functions.Numbers)
        return Response{Result: functions.Multiply(req.Numbers)}, nil
    }
}

func makeAverageEndpoint() kitendpoint.Endpoint {
    return func(ctx context.Context, request interface{}) (interface{}, error) {
        req := request.(*functions.Numbers)
        return Response{Result: functions.Average(req.Numbers)}, nil
    }
}


// Wraps the DecodeRequest function to match Go Kit's expected signature
func decodeRequest(_ context.Context, r *http.Request) (interface{}, error) {
    return functions.DecodeRequest(r)
}

func encodeResponse(_ context.Context, w http.ResponseWriter, response interface{}) error {
    return json.NewEncoder(w).Encode(response)
}

func main() {

    http.Handle("/compute", kithttp.NewServer(
        makeComputeEndpoint(),
        decodeRequest,
        encodeResponse,
    ))

    http.Handle("/multiply", kithttp.NewServer(
        makeMultiplyEndpoint(),
        decodeRequest,
        encodeResponse,
    ))

    http.Handle("/average", kithttp.NewServer(
        makeAverageEndpoint(),
        decodeRequest,
        encodeResponse,
    ))


    http.ListenAndServe(":8000", nil)
}
