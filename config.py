from os import getenv

API_ID = int(getenv("API_ID", "15350244")) #optional
API_HASH = getenv("API_HASH", "28100f5f7ebbc51d16ca759c87af30dc") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5368154755").split()))
OWNER_ID = int(getenv("OWNER_ID", "1886471878"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Oyehoye143:Oyehoye143@cluster0.eth7a3p.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5423617634:AAGilf7a2Od1S7mK9ozNIl6VkN1q9zXcAZE")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "ʀᴏᴍᴇᴏʙᴏᴛ")
PM_LOGGER = getenv("PM_LOGGER", "-1001882915379")
LOG_GROUP = getenv("LOG_GROUP", "-1001882915379")
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/Rj-sgshsb/Romeo-UserBot")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBi0s3lEwMxWHG78xM1QTnchztEoKw1l1ns-yswuR1sW7_fzWmn9BFEeCLqKfhaC-_722nVSPV1H_AxTTuwRoXFeNAdb-PFBszcAvKyIohoTnxg8G5CS1iaDxg2L5JMUBlPdZqlDI_oy6FzBHWfb6SOr9Mtb5zBtOLBqKYEcMEY5Z6lO_nGgVT6gahy78GosPp5czTBdrG-AcJj4LTGjsHU1xiZC1L6B-av14T7UsgYltEwmV4UShh_NqYK400rfWKFUg7EkA-AHUlxfNbJ4bccmnZ0phQyKz2Gyn15jhmdFWHnna94wDvWsIzRErsTYE-V3Z7g5p6JI3HQuGyqT3U1cHFGxgA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQBU5MH42OYCYpWQhuSo7e8AHtqUC8rYiGA9cMA4vk31eAqyaoTg0G83jpmRRA9qLUTQvEoi-3w7VtbIYR-MZrfIh9W4_jex5zJm0n7sgim-74QTZEY6LB8QDenE3j1hMioS0fNJkVFy-C8W4BQgJE7nrI6WLKu4Y7yBC3gXiZ6UYM1Ndvu1WdZz_zOFrVbt28XIUencEDK5GbrUMIT05Ci7TUceBAAhdVsQTZYvAzWFKkasR2cMNnZeT4EU1psgSvUOgRitorjliIWyFSrUYKAd6BnBUE7rUgGEIQPgtyexScKFU-GX28lBHELI3oFkJhRUkAjT21bHJZyqHBNSxArAQ-MXXAA")
STRING_SESSION3 = getenv("STRING_SESSION3", "BQBjIgmr51DqgEwxnkGWgAWcuYC0ZiApS7kAoKd6Gnms4yy-Q0wTOwlahRz8BltQejfWnk1sGb_A9Cqk4tngKzNvrtjP-7ZfryTsKbyAxBL9S_LA2shqS4Q5nmkXqeqVBpzH5p1ArUpM8-8inew4ZqH3MxJzX41ZHRCqS38l46mBu3dW8lhyOMoiUPJon0B7TK-sldA5ljhoqT2CWJZfj2aOyxZ7MPiJm1YshkQTi3QKUmhfyXM2Tq2pQaFCUjpX0BU8I18v6aoIOkiJbcOwWxQWiz4N04kyft9ObNPO2ELJf99KIQUPULP0Appqcp93scY_HkLoQk5TmMGWULq6llINYmw6cAA")
STRING_SESSION4 = getenv("STRING_SESSION4", "BQBWFk2RLe0Tq6lG1DmexymPUbYUtOteuhrZt7IBTGa9sGz_sfsoK7kV8rODBaizJ3k8ePNIEWkz3RDIVmvmdH185c3gyMktr-WOSX5G64qOqAA8Bj_BqScDyR2NVQV_CeTRI1MSylQOQgtqd02e_YjBcCwLeCBerbxnPc-3ySxd80q9GZav2r_TmZBoxLXhfb1RLrKHG4CSglBK8bAdo_ztWSPuveJ8mrROgyWRgKq5e3ZGhl1dafgl7OObr8zL6W5orUEqtAgVJ9dwNbXTs8O9TUHa-uTri-vdLRzICDHITPn8hBZB7y_9s8R2bJSmrNtLp2trGzINx2bGyjxUmRcHRyGowQA")
STRING_SESSION5 = getenv("STRING_SESSION5", "BQBGEcBh1F4hxx_6v5dzbbxYUMmLUyZxbVzOUvL0mbE39OIkrDDZTDNUOcbwkTI3OJKFFMOT0CLQ_Kllv4F2y9b8rU3mLwTEGtdqhXVlJcX4jIIcdQz7SIN8whoyllyEMwi1b3cbQ6n_emMy2CfnK4sjqovNr4R-HkAWjJBFbIqFy29w8jtA70lFOGCdLC1u7Le1AtrRSH9dQkQvNxIvy9ALJnq-bBSZvkogBl-zAOFwYN5SIUirhUFSjGyVAsUVty1cImza74eXLCHYBRZIxWP14ho3oZCwt97U7JuDUpDmZaayDtNh8tbvOVOKp0swp5KbJNc1eva9VZ7SqftI8ghjAAAAATGbVHYA")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
