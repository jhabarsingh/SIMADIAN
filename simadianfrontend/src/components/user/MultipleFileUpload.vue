<template>
  <div
	v-if="hidden"
  >
    <v-card class="text-center"
      style="margin: 0px auto 10px auto;padding:10px;display:flex;justify-content:center;"
      max-width="700px"
    >
      <v-file-input
          multiple
          label="Upload Files"
          v-model="files"
      ></v-file-input>
      <v-btn
          class="mx-2"
          fab
          dark
          small
          color="primary"
          @click="upload"
      >
      <v-icon dark>
        mdi-upload
        </v-icon>
      </v-btn>
    </v-card>
    <v-progress-linear
      indeterminate
      color="yellow darken-2"
      style="max-width:700px; margin:auto;"
      v-if="show"
    ></v-progress-linear>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    files: null,
    show: false,
    hidden: true
  }),
  methods: {
    getExtension(filename) {
      var parts = filename.split('.');
      return parts[parts.length - 1];
    },

    isVideo(filename) {
      var ext = this.getExtension(filename);
      switch (ext.toLowerCase()) {
        case 'm4v':
        case 'avi':
        case 'mpg':
        case 'mp4':
        case 'mp3':
        case '3gp':
          // etc
          return true;
      }
      return false;
    },
    async upload() {
      let url = this.$store.state.URL + "items/files/upload";
      let token = localStorage.getItem("access");
      this.show = true;
      console.log(this.files);
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': 'Bearer ' + token
        }
      }


      for(let i=0; i<this.files.length; i++) {
        let file = this.files[i];
        if(!this.isVideo(file.name)) continue;
        var formData = new FormData();
        formData.append("file", file);
        
        let res = await axios.post(url, formData, config)
        console.log(res);
      }

      this.show = false;
    }
  },

  created () {
	if(localStorage.getItem("access")) {
	 	// Do Nothing
	}
	else {
		this.hidden = false;
        }

  }
}
</script>
