package main

import (
    "github.com/beego/beego/v2/server/web"
    "app/functions"
)

type AppController struct {
    web.Controller
}


func (c *AppController) Compute() {
    nums, err := functions.DecodeRequest(c.Ctx.Request)
    if err != nil {
        c.Data["json"] = map[string]string{"error": err.Error()}
    } else {
        c.Data["json"] = map[string]interface{}{ "result": functions.Compute(nums.Numbers)}
    }
    c.ServeJSON()
}

func (c *AppController) Multiply() {
    nums, err := functions.DecodeRequest(c.Ctx.Request)
    if err != nil {
        c.Data["json"] = map[string]string{"error": err.Error()}
    } else {
        c.Data["json"] = map[string]interface{}{ "result": functions.Multiply(nums.Numbers)}
    }
    c.ServeJSON()
}

func (c *AppController) Average() {
    nums, err := functions.DecodeRequest(c.Ctx.Request)
    if err != nil {
        c.Data["json"] = map[string]string{"error": err.Error()}
    } else {
        c.Data["json"] = map[string]interface{}{ "result": functions.Average(nums.Numbers)}
    }
    c.ServeJSON()
}


func main() {
    web.BConfig.Listen.HTTPPort = 8000


    web.Router("/compute", &AppController{}, "post:Compute")

    web.Router("/multiply", &AppController{}, "post:Multiply")

    web.Router("/average", &AppController{}, "post:Average")

    web.Run()
}
