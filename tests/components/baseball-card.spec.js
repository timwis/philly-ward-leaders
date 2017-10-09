import { mount } from 'vue-test-utils'
import { createRenderer } from 'vue-server-renderer'

import BaseballCard from '../../src/components/baseball-card/index.vue'

describe('Baseball card', () => {
  it('Matches snapshot', () => {
    const propsData = {
      name: 'John Doe',
      ward: 1,
      party: 'democratic',
      photoUrl: 'https://example.com/image.png',
      registeredVotersParty: 1000,
      turnoutParty: 400,
      turnoutTotal: 600,
      divisionCount: 30,
      committeePersonCount: 25
    }
    const wrapper = mount(BaseballCard, {
      propsData,
      stubs: ['router-link']
    })
    const renderer = createRenderer()
    renderer.renderToString(wrapper.vm, (err, str) => {
      expect(str).toMatchSnapshot()
    })
  })
})
