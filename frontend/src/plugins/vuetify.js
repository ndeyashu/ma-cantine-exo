import Vue from "vue"
import Vuetify from "vuetify/lib/framework"
import theme from "@/theme"
import { VBtn, VCard, VRadio, VCheckbox } from "vuetify/lib"
import remixJson from "./remix.json"
import { Resize, ClickOutside, Scroll } from "vuetify/lib/directives"

// Necessary for now as a workaround for a Vuetify bug: Check again
// after next Vuetify update : https://github.com/vuetifyjs/vuetify/issues/4871
Vue.use(Vuetify, {
  directives: {
    Resize,
    ClickOutside,
    Scroll,
  },
})

// Defaults to conform to DSFR
VBtn.options.props.ripple.default = false
VBtn.options.props.elevation.default = 0
VCard.options.props.ripple.default = false
VRadio.options.props.ripple.default = false
VCheckbox.options.props.ripple.default = false

export default new Vuetify({
  theme: theme,
  iconfont: "md",
  breakpoint: {
    mobileBreakpoint: "sm",
  },
  /*
  remixJson contains a key-value pair of icon names and svg paths. These correspond to the icons
  on https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/icones.
  To use them, instead of using the "mdi-" prefix, just append a dollar sign. For example, to use
  icon "cloudy-2-fill" you can use "<v-icon>$cloudy-2-fill</v-icon>".

  Note that not all Remix icons are included, only those chosen by the DSFR. MDI icons are still
  available.
  */
  icons: {
    iconfont: "mdi",
    values: remixJson,
  },
})
