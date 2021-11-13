import { createApp } from 'vue'
import App from './App.vue'

import BaseButton from "./components/UI/BaseButton.vue";
import BaseCheckbox from "./components/UI/BaseCheckbox.vue";
import BaseTableRow from "./components/UI/BaseTableRow.vue";

const app = createApp(App);
app.component('base-button', BaseButton);
app.component('base-checkbox', BaseCheckbox);
app.component('base-table-row', BaseTableRow);
app.mount('#app');
