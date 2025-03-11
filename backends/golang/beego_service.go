package main

import (
    "github.com/beego/beego/v2/server/web"
    "app/functions"
)

type AppController struct {
    web.Controller
}


func (c *AppController) Compute() {
    items, err := functions.DecodeRequest(c.Ctx.Request)
    if err != nil {
        c.Data["json"] = map[string]string{"error": err.Error()}
    } else {
        c.Data["json"] = map[string]interface{}{ "result": functions.Compute(items.Items)}
    }
    c.ServeJSON()
}

func (c *AppController) Multiply() {
    items, err := functions.DecodeRequest(c.Ctx.Request)
    if err != nil {
        c.Data["json"] = map[string]string{"error": err.Error()}
    } else {
        c.Data["json"] = map[string]interface{}{ "result": functions.Multiply(items.Items)}
    }
    c.ServeJSON()
}

func (c *AppController) Average() {
    items, err := functions.DecodeRequest(c.Ctx.Request)
    if err != nil {
        c.Data["json"] = map[string]string{"error": err.Error()}
    } else {
        c.Data["json"] = map[string]interface{}{ "result": functions.Average(items.Items)}
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