package main

import (
    "app/functions"
    "github.com/gofiber/fiber/v2"
    "bytes"
    "net/http"
)


func ComputeHandler(c *fiber.Ctx) error {
    // Convert fasthttp request body to net/http request
    body := c.Body()
    req, err := http.NewRequest("POST", "/", bytes.NewReader(body))
    if err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
    }

    nums, err := functions.DecodeRequest(req)
    if err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
    }

    return c.JSON(fiber.Map{"result": functions.Compute(nums.Numbers)})
}

func MultiplyHandler(c *fiber.Ctx) error {
    // Convert fasthttp request body to net/http request
    body := c.Body()
    req, err := http.NewRequest("POST", "/", bytes.NewReader(body))
    if err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
    }

    nums, err := functions.DecodeRequest(req)
    if err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
    }

    return c.JSON(fiber.Map{"result": functions.Multiply(nums.Numbers)})
}

func AverageHandler(c *fiber.Ctx) error {
    // Convert fasthttp request body to net/http request
    body := c.Body()
    req, err := http.NewRequest("POST", "/", bytes.NewReader(body))
    if err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
    }

    nums, err := functions.DecodeRequest(req)
    if err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
    }

    return c.JSON(fiber.Map{"result": functions.Average(nums.Numbers)})
}


func main() {
    app := fiber.New()

    
    app.Post("/compute", ComputeHandler)
    
    app.Post("/multiply", MultiplyHandler)
    
    app.Post("/average", AverageHandler)
    

    app.Listen(":8000")
}