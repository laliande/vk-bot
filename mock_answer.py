def return_answer(token, group_id):
    data = {"about_group": {
        "token": token,
            "group_id": group_id,
            "version_api": "5.120"
            }, "elements": [
            {
                "buttons": [
                    {
                        "button_id": 1,
                        "inline": True,
                        "color": "primary",
                        "text": "button qqqq",
                        "link": "link",
                        "one_time": False,
                        "action": "text",
                        "if_no_button_type": "standart",
                        "if_no_button": 1
                    },
                    {
                        "button_id": 2,
                        "inline": True,
                        "color": "primary",
                        "text": "button2",
                        "link": "link",
                        "one_time": False,
                        "action": "text",
                        "if_no_button_type": "standart",
                        "if_no_button": 1
                    },
                    {
                        "button_id": 3,
                        "inline": True,
                        "color": "primary",
                        "text": "button3",
                        "link": "link",
                        "one_time": False,
                        "action": "text",
                        "if_no_button_type": "standart",
                        "if_no_button": 1
                    },
                    {
                        "button_id": 4,
                        "inline": True,
                        "color": "primary",
                        "text": "button4",
                        "link": "link",
                        "one_time": False,
                        "action": "text",
                        "if_no_button_type": "standart",
                        "if_no_button": 1
                    }
                ],
                "messages": [
                    {
                        "message_id": 1,
                        "text": "screen 0",
                        "attach": ""
                    },
                    {
                        "message_id": 2,
                        "text": "screen 1",
                        "attach": ""
                    },
                    {
                        "message_id": 3,
                        "text": "screen 2",
                        "attach": "photo226523848_456239446"
                    },
                    {
                        "message_id": 4,
                        "text": "screen 3",
                        "attach": "video-76456136_456243700"
                    },
                    {
                        "message_id": 5,
                        "text": "screen 4",
                        "attach": "audio-790272_456239109"
                    }
                ]
            }
            ],
            "actions": [
            {
                "step_id": 0,
                "message_id": 1,
                "kit_buttons": [
                    {
                        "line": 1,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 1,
                                "next_step_id": 1
                            }
                        ]
                    },
                    {
                        "line": 2,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 3,
                                "next_step_id": 1
                            },
                            {
                                "id": 2,
                                "button_id": 4,
                                "next_step_id": 1
                            }
                        ]
                    }
                ]
            },
        {
                "step_id": 1,
                "message_id": 2,
                "kit_buttons": [
                    {
                        "line": 1,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 1,
                                "next_step_id": 2
                            },
                            {
                                "id": 2,
                                "button_id": 2,
                                "next_step_id": 2
                            }
                        ]
                    },
                    {
                        "line": 2,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 3,
                                "next_step_id": 2
                            },
                            {
                                "id": 2,
                                "button_id": 4,
                                "next_step_id": 2
                            }
                        ]
                    }
                ]
            },
        {
                "step_id": 2,
                "message_id": 3,
                "kit_buttons": [
                    {
                        "line": 1,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 1,
                                "next_step_id": 3
                            },
                            {
                                "id": 2,
                                "button_id": 2,
                                "next_step_id": 3
                            }
                        ]
                    },
                    {
                        "line": 2,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 3,
                                "next_step_id": 3
                            },
                            {
                                "id": 2,
                                "button_id": 4,
                                "next_step_id": 3
                            }
                        ]
                    }
                ]
            },
        {
                "step_id": 3,
                "message_id": 4,
                "kit_buttons": [
                    {
                        "line": 1,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 1,
                                "next_step_id": 4
                            }
                        ]
                    }
                ]
            },
        {
                "step_id": 4,
                "message_id": 5,
                "kit_buttons": [
                    {
                        "line": 1,
                        "buttons": [
                            {
                                "id": 1,
                                "button_id": 1,
                                "next_step_id": 0
                            }
                        ]
                    }
                ]
            }
    ]
    }
    return data
