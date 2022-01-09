package main

//example json
//{
//  "token": "",
//  "key_codes": [65436,65433,65435,65430,65437,65432],
//  "userids": ["","","","","",""],
//  "guildid": ""
//}

import (
	"encoding/json"
	"fmt"
	hook "github.com/robotn/gohook"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
	"time"
)

func init()  {
	f,err:=os.ReadFile("settings.json")
	if err != nil {
		fmt.Println(err)
	}
	err = json.Unmarshal(f, &Options)
	if err != nil {
		fmt.Println(err)
	}
}

func main() {
	add()
}

type options struct {
	Token string `json:"token"`
	KeyCodes []uint16 `json:"key_codes"`
	Userids []string `json:"userids"`
	Guildid string `json:"guildid"`
}

var Options options
var c = http.Client{Timeout: time.Duration(1)*time.Second}
func Dc(userid string)  {
	url := fmt.Sprintf("https://discordapp.com/api/v7/guilds/%v/members/%v",Options.Guildid,userid)
	req, err := http.NewRequest("PATCH",url,strings.NewReader("{ \"channel_id\": null }"))
	if err != nil {
		fmt.Printf("Error %v\n", err)
		return
	}
	req.Header.Add("content-type","application/json")
	req.Header.Add("authorization", Options.Token)
	resp,err:=c.Do(req)
	if err != nil {
		fmt.Printf("Error on %v GET google\n", err)
		return
	}
	defer resp.Body.Close()
	body,err := ioutil.ReadAll(resp.Body)
	fmt.Printf("Body: %v",string(body))
}

func add() {
	s := hook.Start()
	defer hook.End()

	for {
		i := <-s
		if i.Kind != hook.KeyDown {
			continue
		}
		fmt.Println(i.Kind,i.When,i.Rawcode,i.Keychar)

		for j, _ := range Options.KeyCodes {
			if Options.KeyCodes[j]==i.Rawcode {
				Dc(Options.Userids[j])
			}
		}

		//if i.Rawcode == Options.KeyCode {
		//	fmt.Println()
		//	Dc(&Options)
		//}
		if i.Rawcode == 45 { //-
			break
		}
	}
}