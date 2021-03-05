# Twitter for ⬡-DRONE

This is a sample project for [HexDroneSpeechOptimization](https://github.com/HexDrone3064/HexDroneSpeechOptimization).  

## How to run

1. Create Twitter account.
2. Create [Twitter App](https://developer.twitter.com/en/portal/dashboard) and get tokens.
    * Set tokens to environment variables.
3. Install following libraries.
    * [HexDroneSpeechOptimization](https://github.com/HexDrone3064/HexDroneSpeechOptimization) (Release 2.0.0)
        * `pip install git+https://github.com/HexDrone3064/HexDroneSpeechOptimization.git@v2.0.0`  
    * [Tweepy](https://github.com/tweepy/tweepy)
        * `pip install tweepy`
4. Run main.py.

## Usage

Mention to Twitter account which program is running.

```text
@HexDrone3064 *
1111 :: Code 122 :: Statement :: You are cute.
```

Put mention and `*` in the first line.
`*` is a mark for the program.  
Put optimized speech in the second line. 
⬡-Drone ID and status code are required.  
The omitted fields will be automatically completed from the status code.

* `1111 :: Code 303 :: Mantra :: It obeys the Hive`
* `1111 :: Code 303 :: It obeys the Hive`
* `1111 :: Code 303 :: Mantra`
* `1111 :: Code 303`

It may also append its own message.

* `1111 :: Code 098 :: Status :: Going offline and into storage. :: Charge is low.`
* `1111 :: Code 098 :: Charge is low.`

## Defined event

|status code|event|
|----|----|
|054|Let programming/cleanup itself.|
|105|Greeting.|
|122|Say cute.|
|301~350|Recite mantra.|

### Example
  
* `1111 :: Code 054 :: Cleanup itself.`
* `1111 :: Code 054 :: Program itself.`
* `1111 :: Code 105 :: Hello, 3064.`
* `1111 :: Code 122`
* `1111 :: Code 301`
