import { NgModule } from '@angular/core';
// import { TaskItemComponent } from 'src/app/tasks/components/task-item/task-item.component';
import { SharedModule } from 'src/app/shared/shared.module';
import { TaskItemComponent } from './task-item/task-item.component';

@NgModule({
  declarations: [TaskItemComponent],
  imports: [SharedModule],
  exports: [TaskItemComponent]
})
export class ComponentsModule {}
