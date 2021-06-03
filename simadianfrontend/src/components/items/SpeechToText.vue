<template>
<div
  style="margin-top:5px"
>   
    <v-card
        max-width="150px"
    >
                <div
                  style="padding:1px 7px;display:flex;justify-content:space-around;"
                >
                  <v-btn
                    dark
                    @click.stop="toggle ? endSpeechRecognition() : startSpeechRecognition()"
                    icon
                    :color="!toggle ? 'grey' : (speaking ? 'red' : 'red darken-3')"
                    :class="{'animated infinite pulse': toggle}"
                  >
                    <v-icon>{{toggle ? 'mdi-microphone-off' : 'mdi-microphone'}}</v-icon>
                  </v-btn>
                  <v-btn
                    dark
                    @click="clearSentences"
                    icon
                    :color="!toggle ? 'grey' : (speaking ? 'red' : 'red darken-3')"
                    :class="{'animated infinite pulse': toggle}"
                  >
                   <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </div>
    </v-card>
</div>
</template>

<script>

let SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
let recognition = SpeechRecognition? new SpeechRecognition() : false

export default {
  props: {
    lang: {
      type: String,
      default: 'en-US'
    }
  },
  data () {
    return {
      error: false,
      speaking: false,
      toggle: false,
      runtimeTranscription: '',
      sentences: [],
      text: ""
    }
  },
  watch: {
    'text' (val) {
      this.$store.state.message = val;
    }
  },
  methods: {
    clearSentences () {
      this.sentences = [];
      this.text = "";
      this.$store.state.message = "";
    },
    checkCompatibility () {
      if (!recognition) {
        this.error = 'Speech Recognition is not available on this browser. Please use Chrome or Firefox'
      }
    },
    endSpeechRecognition () {
      recognition.stop()
      this.toggle = false;
    },
    startSpeechRecognition () {
      if (!recognition) {
        this.error = 'Speech Recognition is not available on this browser. Please use Chrome or Firefox'
        return false
      }
      this.toggle = true
      recognition.lang = this.lang
      recognition.interimResults = true

      recognition.addEventListener('speechstart', event => {
        this.speaking = true
      })

      recognition.addEventListener('speechend', event => {
        this.speaking = false
      })

      recognition.addEventListener('result', event => {
        const text = Array.from(event.results).map(result => result[0]).map(result => result.transcript).join('')
        this.runtimeTranscription = text
      })

      recognition.addEventListener('end', () => {
        if (this.runtimeTranscription !== '') {
          this.sentences.push(this.capitalizeFirstLetter(this.runtimeTranscription))
          this.text = this.sentences.join('. ')
        }
        this.runtimeTranscription = ''
        recognition.stop()
        if (this.toggle) {
          // keep it going.
          recognition.start()
        }
      })
      recognition.start()
    },
    capitalizeFirstLetter (string) {
      return string.charAt(0).toUpperCase() + string.slice(1)
    }
  },
  mounted () {
    this.checkCompatibility()
  }
}
</script>